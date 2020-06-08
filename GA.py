data = [
    ['top', 't-shirt', ['dark', 'bright'], ['casual', 'sportswear'], 0.0],
        ['top', 'blouse', ['bright'], ['business', 'evening'], 200.0],
        ['top', 'bodysuit', ['dark'], ['casual', 'evening'], 150.0],
        ['top', 'sleeveless', ['dark'], ['casual'], 110.0],
        ['top', 'tank', ['bright'], ['casual', 'sportswear'], 70.0],
        ['top', 'sweater', ['dark'], ['casual', 'business'], 200.0],
        ['top', 'vest', ['dark'], ['business'], 300.0],
        ['top', 'blazer', ['dark'], ['business'], 430.0],
        ['top', 'jacket', ['bright'], ['casual'], 0.0],
        ['top', 'hoodie', ['bright', 'dark'], ['sportswear'], 230.0],
        ['top', 'cardigan', ['bright'], ['casual'], 300.0],
        ['bottom', 'jeans', ['dark'], ['casual'], 150.0],
        ['bottom', 'knee length pant', ['bright'], ['casual'], 220.0],
        ['bottom', 'ankle length pant', ['dark'], ['business'], 0.0],
        ['bottom', 'high waist pant', ['bright'], ['business'], 150.0],
        ['bottom', 'legging', ['dark'], ['casual'], 100.0],
        ['bottom', 'sweatpants', ['bright'], ['casual'], 100.0],
        ['bottom', 'wide leg pants', ['dark', 'bright'], ['business', 'evening'], 500.0],
        ['bottom', 'maxi skirt', ['bright'], ['evening'], 500.0],
        ['bottom', 'midi skirt', ['dark'], ['business'], 0.0],
        ['bottom', 'short skirt', ['bright'], ['casual'], 400.0],
        ['shoes', 'sandals', ['dark'], ['casual', 'evening'], 120.0],
        ['shoes', 'sneakers', ['bright'], ['sportswear', 'casual'], 300.0],
        ['shoes', 'high heel', ['dark'], ['evening'], 0.0],
        ['shoes', 'mid heel', ['bright'], ['casual', 'business'], 400.0],
        ['shoes', 'low heel', ['dark'], ['business'], 150.0],
        ['shoes', 'flat', ['bright'], ['casual'], 0.0],
        ['shoes', 'boots', ['dark'], ['casual'], 500.0],
        ['neck', 'necklace', ['dark'], ['business', 'evening'], 150.0],
        ['neck', 'choker', ['bright'], ['sportswear', 'casual'], 0.0],
        ['neck', 'scarf', ['bright'], ['casual', 'evening'], 250.0],
        ['neck', 'tie', ['dark'], ['business'], 100.0],
        ['neck', 'bow tie', ['dark'], ['business', 'evening'], 100.0],
        ['handbag', 'backpack', ['bright'], ['sportswear'], 100.0],
        ['handbag', 'purse', ['bright'], ['business'], 600.0],
        ['handbag', 'clutch', ['dark'], ['evening'], 500.0],
        ['handbag', 'belt bag', ['dark'], ['casual'], 300.0],
        ['handbag', 'cross bag', ['dark'], ['business'], 0.0]]

import numpy as npy
import random

class GeneticAlgorithm:
    data = npy.array(data)


    def populationInitialisation(self, popSize):
        initialpop = []
        for i in range(popSize):
            gene1 = random.randint(0, 10)
            gene2 = random.randint(11, 21)
            gene3 = random.randint(22, 32)
            gene4 = random.randint(33, 43)
            gene5 = random.randint(44, 55)
            fitValue = self.FitnessCalculation([gene1, gene2, gene3, gene4, gene5])
            individual = [gene1, gene2, gene3, gene4, gene5, fitValue]
            initialpop.append(individual)
        return initialpop

    def populationSort(self, pop):
        pop.sort(key=self.getFitnessValue, reverse=True)

    def getFitnessValue(self, individual):
        return individual[5]

    def FitnessCalculation(self, individual):
        fitVal1 = 0
        fitVal2 = 0
        fitVal3 = 0
        sumPrice = 0
        for i in individual:
            if dress_code in data[i, 3]:
                fitVal1 = fitVal1 + 1
            if color in data[i, 2]:
                fitVal2 = fitVal2 + 1
            sumPrice = sumPrice + float(data[i, 4])
            if price <= sumPrice:
                fitVal3 = fitVal3 + 1

        fitnessValue = (fitVal1*0.4 + fitVal2*0.2 + fitVal3*0.4)/5
        return fitnessValue

    def roulette_wheel_selection(self, pop, popSize):

        #calculate the fitness of each chromosome

        fitValues = []
        i = 0
        while i < popSize:
            fitValues.append(pop[i][5])
            i = i + 1
        sumFitnesses = sum(fitValues)

        #calculate the probability of selection of each chromosome

        problist = []
        prouviousProbability = 0
        for i in range(popSize):
            Pr = prouviousProbability + (fitValues[i] / sumFitnesses)
            problist.append(Pr)
            prouviousProbability = Pr

        for i in range(popSize):
            if random.random() <= problist[i]:
                return i

    def crossover(self, par1, par2):
        child = []

        start_gene = int(random.random() * len(par1) - 1)

        for i in range(0, start_gene):
            child.append(par1[i])
        for i in range(start_gene, len(par1) - 1):
            child.append(par2[i])

        child.append(self.FitnessCalculation(child))
        return child

    def mutation(self, individual, m):
        for gene in range(len(individual) - 1):
            if (random.random() < m):
                if gene == 0:
                    individual[0] = random.randint(0, 10)
                if gene == 1:
                    individual[1] = random.randint(11, 20)
                if gene == 2:
                    individual[2] = random.randint(21, 27)
                if gene == 3:
                    individual[3] = random.randint(28, 32)
                if gene == 4:
                    individual[4] = random.randint(33, 37)
        individual[5] = self.FitnessCalculation(individual[0:5])
        return individual

    def replacment(self, child, population):
        population.append(child)
        self.populationSort(population)
        population.pop(-1)
        return population

if __name__ == '__main__':

    dress_code = input("Enter the dress code")
    color = input("Enter which color [light, dark]")
    price = input("Enter your budhet [ SAR 0.0 – SAR ∞ ]")


    popSize = 100
    population = GeneticAlgorithm.populationInitialisation(popSize)
    GeneticAlgorithm.populationSort(population)

    plotgenerations = []
    plotfitness = []

    i = 0

    for i in range(20000):
        p1 = GeneticAlgorithm.roulette_wheel_selection(population, popSize)
        p2 = GeneticAlgorithm.roulette_wheel_selection(population, popSize)

        if random.random() < 0.75:
            child = GeneticAlgorithm.crossover(population[p1], population[p2])
            child = GeneticAlgorithm.mutation(child, 0.25)
            GeneticAlgorithm.replacment(child, population)
        plotgenerations.append(i)
        plotfitness.append(population[0][5])
        print("generation number: ", i, "Best individual: ", population[0][0:5], "Best individual: ", population[0][5])