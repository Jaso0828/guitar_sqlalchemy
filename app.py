from config import AppConfig
from infrastructures.base_repository import BaseRepository
from core.guitars.guitars import Guitar
import os


def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    repo = BaseRepository()
    repo.db_seed()

    guitar_category_electric = repo.guitar_category_repo.get_by_name('Electric')
    guitar_type_1 = repo.guitar_type_repo.get_by_name('Solid-body electric')
    guitar = Guitar(
        name = 'Fender Stratocaster',
        year = 1968,
        price = 5000.50,
        guitar_category = guitar_category_electric,
        guitar_type = guitar_type_1
    )

    guitar = repo.guitar_repo.add(guitar)




if __name__ == "__main__":
    main()