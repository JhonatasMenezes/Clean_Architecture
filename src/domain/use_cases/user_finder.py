from abc import ABC, abstractmethod
from typing import Dict


class UserFinderInterface(ABC):

    @abstractmethod
    def find(self, first_name: str) -> Dict: pass
