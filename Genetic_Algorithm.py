import numpy as np
import random
import math
from random import shuffle

print ("Colours encoding:" + "\n" + "Blue 00" + "\n" + "Red 01" + "\n"+"Green 10"+ "\n"+"Yellow 11")


def parents_fitness_score(ga_population, cities_map):  
    parents_score = [] 
    for parent in ga_population: #Candidate solution is a candiate parent 
        score = 0
        for city_index in range(cities_map.shape[0]): 
            for other_city in range(cities_map.shape[0]):               
                if cities_map[city_index, other_city] == 1: 
                    if (parent[city_index*2] != parent[other_city*2] or 
                            parent[(city_index*2)+1] != parent[(other_city*2)+1]):
                        score=score+1
        parents_score.append(score)              
    return parents_score

def  roulette_wheel_parents_selection(parents_score): 
    
    number_of_mates = int(len(parents_score) / 2)
    parents_total_fitness = float(sum(parents_score))
    parents_relative_fitness = [parent_fitness/parents_total_fitness for parent_fitness in parents_score]
    parents_cumulative_probability = [sum(parents_relative_fitness[ : i+1]) for i in range(len(parents_relative_fitness))]
    
    parents_indexes_list = []
    #numbers belong to [0.0,1.0)
    random_numbers = []
    for iteration in range(2):
        random_numbers.append(random.random())
        random_numbers.sort() 
    choose_number_parent1 = random_numbers[0]
    choose_number_parent2 = random_numbers[1]
    parent1_selected = False
    parent2_selected = False
    
    while number_of_mates != 0:
        for parent_index in range(len(parents_cumulative_probability)):
            if (choose_number_parent1 <= parents_cumulative_probability[parent_index] and 
                    parent1_selected == False):  
                parent1_selected = True
                parent1_index = parent_index
                parents_indexes_list.append(parent1_index)

            if (choose_number_parent2 <= parents_cumulative_probability[parent_index]):
                parent2_index = parent_index
                while(parent1_index == parent2_index):
                    choose_number_parent2=random.random()
                    for parent_index2 in range(len(parents_cumulative_probability)):
                        if (choose_number_parent2 <= parents_cumulative_probability[parent_index2]):
                            parent2_index = parent_index2
                            break 
                parents_indexes_list.append(parent2_index)
                parent2_selected = True
                break 
            
        if (parent2_selected) :
            break
                            
        number_of_mates = number_of_mates - 1
        
    return parents_indexes_list

def single_point_crossover(selected_parents, ga_population): #the crossover point is the middle point
    offspring = np.zeros([len(selected_parents), ga_population.shape[1]], dtype=int) 
    half_parent_size = int(ga_population.shape[1] / 2)
    for index in range(0,len(selected_parents), 2): 
        offspring[index, 0 : half_parent_size] = ga_population[selected_parents[index], 0 : half_parent_size] 
        offspring[index, half_parent_size:] = ga_population[selected_parents[index + 1], half_parent_size:] 
        offspring[index + 1, 0 : half_parent_size] = ga_population[selected_parents[index + 1], 0 : half_parent_size]
        offspring[index + 1, half_parent_size:] = ga_population[selected_parents[index], half_parent_size:]
        
    return offspring

def mutation(offspring): #10% mutation to children
    number_of_mutations = int(math.ceil(offspring.shape[0]*0.1)) 
    
    for mutation_index in range(number_of_mutations): 
        selected_offspring = random.randint(0, offspring.shape[0]-1) 
        selected_offspring_bit = random.randint(0, offspring.shape[1]-1) 
        if offspring[selected_offspring, selected_offspring_bit] == 0:
            offspring[selected_offspring, selected_offspring_bit] = 1
        else:
            offspring[selected_offspring, selected_offspring_bit] = 0
            
    return offspring


def citiesmap_initiation(choice):
    
    if choice == 1:
        number_of_cities = 16 
        ga_population_size = 4 * number_of_cities 
        cities_map = np.array(
            [
                [0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1],[0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]
        )
        
    else: 
        while True:
            try:
                number_of_cities = int(input("Please enter the size of the map: ")) 
                break
            except ValueError as e:
                print ("Please use only numbers, not characters")
                
        ga_population_size = number_of_cities * 4  
        cities_map = np.zeros([number_of_cities, number_of_cities], dtype=int)
        print ("Please type the relations between cities on the map. When i=j, the value is automatically zero")
        #Only the values above the main diagonal of the cities_map matrix are calculated 
        for city_index in range(number_of_cities):
            for other_city in range(city_index + 1, number_of_cities):
                if (city_index == other_city):
                    cities_map[city_index, other_city] = 0
                else:
                    while True:
                        try:
                            print ("Is city ", city_index + 1, " neighbour with ", other_city + 1, " ?")
                            number = int(input("Please enter 0(No) or 1(Yes):"))
                            if (number == 0) or (number == 1) :
                                cities_map[city_index, other_city] = number
                                break
                            else:
                                raise ValueError()
                        except ValueError as e:
                           print ("Please type only numbers(0 or 1)") 
                             
    return number_of_cities,ga_population_size,cities_map

def solution_finder_process(best_score_solution,solution_max_score,ga_population,cities_map):
    
    generation_counter = 0 
    while (best_score_solution[0] != solution_max_score) and (generation_counter<100): 
        parents_score = parents_fitness_score(ga_population,cities_map)
        best_score_solution = (max(parents_score), ga_population[parents_score.index(max(parents_score)), :])
        selected_parents = roulette_wheel_parents_selection(parents_score) 
        offspring = single_point_crossover(selected_parents, ga_population)
        mutated_offspring = mutation(offspring) 
        ga_population = mutated_offspring
        generation_counter += 1
        print("Generations completed :",generation_counter)
    return best_score_solution

def genetic_algorithm_process():
    
    while True:
        try:
            choose_map = int(input("Would you like to use the default map? Type 1 for Yes and 0 for No:"))
            if  (choose_map == 1) or (choose_map == 0):
                break 
            else:
                print("Pleaste answer with 1 or 0")
        except ValueError as e:
            print("Pleaste answer with 1 or 0")
            
    number_of_cities, ga_population_size, cities_map = citiesmap_initiation(choose_map)
    solution_max_score = np.sum(cities_map)
    #Number of possible colours is 4. Every candidate solution needs 2 bits(2^2 bits=4) to define the possible combination of colours, so this is multiplied by the number of cities.
    ga_population = np.random.randint(2, size=(ga_population_size, number_of_cities*2))
    best_score_solution = (0,np.zeros([1, ga_population.shape[1]], dtype=int)) #(0,[0...0])

    return solution_finder_process(best_score_solution, solution_max_score, ga_population, cities_map), solution_max_score

best_score_solution, solution_max_score= genetic_algorithm_process()
print ("Solution found",best_score_solution[1],"with overall score "+str(best_score_solution[0])+"/"+str(solution_max_score))

