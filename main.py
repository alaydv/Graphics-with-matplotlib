import utils.format_population as fpt
import utils.population as pup
import utils.graphs as graph

def run():
    data = fpt.read_csv('./world_population.csv')
    country = input('Ingresa un país => ')
    result = pup.get_population_by_country(data, country)
    if len(result) > 0:
        keys, values = pup.get_population_year(result[0])
        graph.bar_chart(keys, values)


if __name__=='__main__':
    run()