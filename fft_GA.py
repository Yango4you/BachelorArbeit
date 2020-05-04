import csv
import GA
import numpy as np


x = []
y = []

with open("trace_0_1.csv", 'r', encoding='utf-8') as f:

    reader = csv.reader(f)
    header = next(reader)
    tabelle = []

    for zeile in reader:
        str1 = ''.join(zeile)
        spalten = str1.split(";")
        tabelle.append(spalten)

    for i in tabelle:
        x.append(float(i[0]))
        y.append(float(i[1]))


sinFunction_num = 8
koeffizienten_num_per_sinFunction = 3

sol_per_pop = 100
num_parents_mating = 40


pop_size = (sol_per_pop, sinFunction_num, koeffizienten_num_per_sinFunction)
new_population = np.empty(pop_size)
for i in range(sol_per_pop):
    for j in range(sinFunction_num):
        new_population[i][j] = GA.koeffizientenGenertieren(sinFunction_num)[j]
#print(new_population)


num_generations = 5

for i in range(num_generations):
    print("Generation: ", i)
    fitness = GA.cal_pop_fitness(x, y, new_population)
    parents = GA.select_mating_pool(new_population, fitness, num_parents_mating)
    offspring_crossover = GA.crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], pop_size[1], pop_size[2]))
    offspring_mutation = GA.mutation(offspring_crossover)

    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    print("Best Koeffizienten:"+"\n", parents[0])
    print("Max. prominence:", np.min(fitness))

    tNew = GA.tcorrFunction(x, y, parents[0], sinFunction_num)
    GA.ploten(x, y, tNew[0], tNew[1], i)










