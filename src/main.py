from pickle import TRUE
from scrape_each_book import BookScraper
from scraper import FastBookScraper
import argparse


def main(output_file, fast, covers_path):
    """
    Scrape todostuslibros/mas_vendidos website
    """
    if (fast == "TRUE"):
        scraper = FastBookScraper()
    else:
        scraper = BookScraper()

    scraper.scrape()
    scraper.data2csv(output_file)

    if (covers_path != ""):
        scraper.download_covers(output_file, covers_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Escoja el metodo de \
        ejecución o el path al fichero de salida.')
    parser.add_argument('-f', '--fast', type=str, default="TRUE",
                        help="TRUE - Utiliza una version rapida que obtiene \
                            solo los datos más importantes. \
                            FALSE - Utiliza una version más lenta que obtiene \
                            todos los datos.\
                            Por defecto es TRUE")
    parser.add_argument('-o', '--output_filepath', type=str,
                        default="output/Bestsellers.csv",
                        help='FilePath al fichero de salida. Por defecto es \
                            output/Bestsellers.csv')
    parser.add_argument('-d', '--download', type=str,
                        default="",
                        help='Path a la carpeta donde descargar las imagenes \
                            de las cubiertas de los libros. Si el campo esta \
                            vacío no se descargaran las imagenes')
    args = parser.parse_args()

    output_file = args.output_filepath
    fast = args.fast
    covers_path = args.download

    main(output_file, fast, covers_path)
