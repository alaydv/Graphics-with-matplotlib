import utils.format_population as fpt
import utils.population as pup
import utils.graphs as graph

def run():
    data = fpt.read_csv('./world_population.csv')
    labels, values = pup.get_population_by_continent(data)
    graph.pie_chart(labels, values)
    # percentages = pup.get_population_by_continent(data)
    # print(percentages)


if __name__=='__main__':
    run()