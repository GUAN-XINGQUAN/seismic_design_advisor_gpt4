# This file is used to declare all global variables.
# Re-factored by GUAN, XINGQUAN in Feb. 2024

import pandas as pd
import re
from pathlib import Path
from typing import Union

BASE_DIRECTORY = Path.cwd()


class Sections:
    """
    This class stores the section database that do not require users' change.
    """
    def __init__(self, file_path: Union[str, Path]):
        self.dataframe = self.load_data(file_path)

    def load_data(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Given a file path, this function loads it into a pandas dataframe.

        Args:
            file_path: a string or a pathlib.Path object denoting the path to data file.

        Returns:
            a pandas dataframe that contains the content of the data file.

        Raises:
            ValueError: the file paths pointing to files other than JSONL and csv.
        """
        if str(file_path).endswith('csv'):
            return pd.read_csv(file_path, header=0)
        elif str(file_path).endswith('jsonl'):
            return pd.read_json(file_path, lines=True)
        else:
            raise ValueError(f'Unsupported file type: {file_path.suffix}. Only support loading .csv or .jsonl.')

    def get_section_property(self, size: str) -> dict:
        """
        Given a section size, this function returns all its property in a dict format.

        Args:
            size: a string denoting the section size: e.g., "W14X730".

        Returns:
            a dict where key is the section property name and the value is the associated value.
        """
        target_idx = self.dataframe['section size'] == size
        # no such section size exists
        if target_idx.sum() != 1:
            raise ValueError(f'Wrong size no {size} exist in the section database!')
        section_info = self.dataframe.loc[target_idx.idxmax()].to_dict()
        return section_info

    def get_section_depth_weight(self, size: str) -> tuple[int, int]:
        """
        Given a section size (e.g., W14X730), this function extracts its depth and weight.
        Assumption: all sections must be wide flange section.

        Args:
            size: a string denoting the section size, e.g., "W14X730".

        Returns:
            a tuple of two integers where the 1st is the depth and 2nd is the linear weight.

        Raises:
            ValueError: the input size does not follow the wide flange naming convention.
        """
        pattern = r'W(\d+)X(\d+)'
        match = re.search(pattern, size)
        if match:
            depth = int(match.group(1))
            weight = int(match.group(2))
            return depth, weight
        else:
            raise ValueError(f'The input {size} does not follow wide flange section size naming conventions.')

    def get_section_candidates(self, depth: str) -> pd.Series:
        """
        Given a section depth (e.g., W14), this function returns all possible section sizes with this depth.

        Args:
            depth: a string denoting the wide flange section depth, e.g., "W14".

        Returns:
            pd.Series where index is the dataframe index and the value is the section size.
        """
        idx = self.dataframe['section size'].str.startswith(depth)
        candidates = self.dataframe.loc[idx, 'section size']
        return candidates

    def search_member_size(self, property_name: str, property_value: float, candidates: list[str]) -> str:
        """
        Given the threshold on a section property, this function returns the most economic section size that satisfy
        this requirement.

        Args:
            property_name: a string that denotes the column name of dataframe, e.g., "Zx".
            property_value: a float number that denotes the minimum threshold, e.g., 100.0.
            candidates: a list of strings denotes the potential section size candidates, e.g., ["W14X730", "W14X..."]

        Returns:
            a string that denotes the section size satisfying the threshold requirement.

        Raises:
            ValueError: if property_name does not exist in the dataframe.
            ValueError: if filtering with candidates generates empty dataframe.
        """
        if property_name not in self.dataframe.columns:
            raise ValueError(f"Column '{property_name}' does not exist in the dataframe.")
        # Filter by candidate list
        candidate_filter = self.dataframe['section size'].isin(candidates)
        if not candidate_filter.any():
            raise ValueError(f"Candidate '{candidates}' yields empty filtered dataframe. Please check candidates.")
        # Filter by property threshold
        property_filter = self.dataframe[property_name] >= property_value
        # Combine both filters
        filtered_df = self.dataframe.loc[candidate_filter & property_filter, :]
        # When no such section exist --> return the largest section within candidate list
        if filtered_df.empty:
            return self.dataframe.loc[candidate_filter, 'section size'].iloc[0]
        economic_section_size = filtered_df.loc[(filtered_df[property_name] - property_value).idxmin(), 'section size']
        return economic_section_size


if __name__ == '__main__':
    SECTION_DATABASE = Sections(BASE_DIRECTORY / 'section_database' / 'all_sections.jsonl')
    print("Retrieve W14X730: ")
    print(SECTION_DATABASE.get_section_property('W14X730'))
    print("Get candidates of W27: ")
    print(SECTION_DATABASE.get_section_candidates('W27'))
