import pandas as pd
from pathlib import Path
import re
from typing import Union

BASE_DIRECTORY = Path.cwd()

class Sections:
    """
    This class stores the section database that do not require users' change.
    """
    def __init__(self, file_path: Union[str, Path]):
        self.dataframe = self.load_data(file_path)

    def load_data(self, file_path: Union[str, Path]):
        if str(file_path).endswith('csv'):
            return pd.read_csv(file_path, header=0)
        elif str(file_path).endswith('jsonl'):
            return pd.read_json(file_path, lines=True)
        else:
            raise ValueError(f'Unsupported file type: {file_path.suffix}. Only support loading .csv or .jsonl.')

    def get_section_property(self, size: str) -> dict:
        """
        Given a section size, this function returns all its property in a dict format.
        """
        target_idx = self.dataframe['section size'] == size
        # no such section size exists
        if target_idx.sum() != 1:
            raise ValueError(f'Wrong size no {size} exist in the section database!')
        section_info = self.dataframe.loc[target_idx.idxmax()].to_dict()
        return section_info

    def get_section_depth_weight(self, size: str) -> type[int, int]:
        """
        Given a section size (e.g., W14X730), this function extracts its depth and weight.
        Assumption: all sections must be wide flange section.
        """
        pattern = r'W(\d+)X(\d+)'
        match = re.search(pattern, size)
        if match:
            depth = int(match.group(1))
            weight = int(match.group(2))
            return depth, weight
        else:
            raise ValueError(f'The input {size} does not follow wide flange section size naming conventions.')

    def get_section_candidates(self, depth: str) -> list[tuple]:
        """
        Given a section depth (e.g,. W14), this function returns all possible section sizes in a list format.
        Each element in the list has two elements: 1st is the section index and 2nd is the section sizes.
        """
        candidate_index = []
        for indx in section_database['index']:
            match = re.search(target_depth, section_database.loc[indx, 'section size'])
            if match:
                candidate_index.append(indx)
        candidates = section_database.loc[candidate_index, 'section size']
        return candidates


if __name__ == '__main__':
    SECTION_DATABASE = Sections(BASE_DIRECTORY / 'section_database' / 'all_sections.jsonl')
    print("Retrieve W14X730: ")
    print(SECTION_DATABASE.get_section_property('W14X730'))