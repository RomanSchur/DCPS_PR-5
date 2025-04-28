import random
import matplotlib.pyplot as plt
POPULATION_SIZE = 10  # розмір популяції
MAX_POPULATIONS = 15 # максимальна кількість популяцій

CHROMOSOME_LENGTH = 6  # довжина хромосоми
GENE_MIN = 1  # мінімальне значення гена
GENE_MAX = 10  # максимальне значення гена
ELITE_SIZE = 2  # розмір еліти

MUTATION_CHANCE = 3 # шанс мутації
MUTATION_MIN = 1#нижній діапазон шансу мутацій
MUTATION_MAX = 5#верхній діапазон шансу мутацій

def create_initial_population():#функція яка створює початкову популяцію
    start_population=[]
    for _ in range(POPULATION_SIZE):
        chromosom=[]
        for _ in range(CHROMOSOME_LENGTH):
            generate_chromosom=random.randint(GENE_MIN,GENE_MAX)
            chromosom.append(generate_chromosom)
        start_population.append(chromosom)
    #for chromosom in start_population:
        #print(chromosom)
    return start_population

def calculate_chromosom_suitability (start_population):
    res_suitability=[]#список в якому зберігається значення придатності для кожного представника(хромосоми)
    for chromosom in start_population:
        suitability = abs(60-sum(chromosom))
        #print("Придатність для хромосоми: ",suitability)
        res_suitability.append(suitability)
    return res_suitability

def random_choice (population):#функця для рандомного вибору батьків для наступного покоління
    Сhoice=random.choice(population)
    return Сhoice

def crossover (chromosom1,chromosom2):#створення нащадків
    dividing_point=random.randint(1,CHROMOSOME_LENGTH)#точка ділення
    child1=chromosom1[:dividing_point]+chromosom2[dividing_point:]
    child2 = chromosom1[dividing_point:] + chromosom2[:dividing_point]
    return child1, child2
def mutation(chromosom):
    chance=random.randint(1,5)
    if chance == MUTATION_CHANCE:
        gene = random.randint(0, CHROMOSOME_LENGTH - 1)  # індекс гена
        chromosom[gene] = random.randint(GENE_MIN, GENE_MAX)  # значення гена
    return chromosom

def sort_population(population, fitness_values):
    paired_data = list(zip(fitness_values, population))#список пар
    paired_data.sort()
    sorted_fitness_values, sorted_population = zip(*paired_data) #ділмо на два масиви
    return list(sorted_population)

def select_next_generation(population, fitness_values):
    sorted_population = sort_population(population, fitness_values)
    elites = sorted_population[:ELITE_SIZE]
    next_generation = elites.copy()
    while len(next_generation) < POPULATION_SIZE:
        parent1 = random_choice(population)
        parent2 = random_choice(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)

        if len(next_generation) < POPULATION_SIZE:
            next_generation.append(child1)
        if len(next_generation) < POPULATION_SIZE:
            next_generation.append(child2)

    return next_generation

def limit_check(numpop):
    if numpop<MAX_POPULATIONS:
        return 1
    else:
        return 2

def create_graf(fit_values):
    populations = range(len(fit_values))
    plt.plot(fit_values)
    plt.xlabel("Популяція")
    plt.ylabel("Найкраща придатність")
    plt.title("Зміна найкращої придатності з часом")
    plt.xticks(populations)
    plt.show()

def main():
    population = create_initial_population()
    num_populations = 0
    best_fitness_values = []
    while limit_check(num_populations) == 1:
        fitness_values = calculate_chromosom_suitability(population)
        best_index = fitness_values.index(min(fitness_values))
        best_fitness = fitness_values[best_index]
        best_fitness_values.append(best_fitness)
        print(f"Популяція {num_populations}, Придатність: {fitness_values[best_index]}, Хромосома: {population[best_index]}")

        population = select_next_generation(population, fitness_values)

        num_populations += 1
    create_graf(best_fitness_values)

main()