import random
from random import shuffle


def Valid(GeneQueen):
	leg = len(GeneQueen)
	for indce in range(leg):
		for jndce in range(leg):
			deltaGRow = abs(indce - jndce)
			deltaGCol = abs(GeneQueen[indce] - GeneQueen[jndce])
			if (deltaGRow == deltaGCol or GeneQueen[indce] == GeneQueen[
				jndce]) and indce != jndce:
				return False
	return True


def FirstGenerateABoard(BoardSize):
	A_Board = []
	for i in range(1, BoardSize + 1):
		A_Board.append(i)
	random.shuffle(A_Board)
	return A_Board


def fitness_function(QueenBoardState):
	fitness = 0;
	le = len(QueenBoardState)
	for inde in range(le):
		for jnde in range(le):
			deltaRow = abs(inde - jnde)
			deltaCol = abs(QueenBoardState[inde] - QueenBoardState[jnde])
			if (deltaRow != deltaCol and QueenBoardState[inde] != QueenBoardState[
				jnde]) and inde != jnde:
				fitness = fitness + 1
	return fitness


def crossOver(Gene1, Gene2):
	genSize = len(Gene1)
	crossPoint = random.randint(0, genSize - 1)
	NewGene1 = []
	NewGene2 = []
	for ci in range(crossPoint):
		NewGene1.append(Gene2[ci])
		NewGene2.append(Gene1[ci])
	
	for cj in range(crossPoint, len(Gene1)):
		NewGene1.append(Gene1[cj])
		NewGene2.append(Gene2[cj])
	
	return NewGene1, NewGene2


def mutate(crossOveredGene):
	geneSize = len(crossOveredGene)
	indeks = random.randint(0, geneSize - 1)
	jndeks = random.randint(1, geneSize)
	newGene = list(crossOveredGene)
	newGene[indeks] = jndeks
	return newGene


def chooseBest(Genes, fit_value):
	siz = 0
	for inds in range(len(Genes)):
		Genes[inds].append(fit_value[inds])
	siz = len(Genes[0]) - 1
	Genes.sort(key=lambda Genes: Genes[siz])
	for jnds in range(len(Genes)):
		Genes[jnds].pop(siz)
	Genes.reverse()
	fit_value.sort()
	fit_value.reverse()
	return Genes, fit_value


def Genetic_Algorithm(BoardsSize):
	Genes_Arrays = []
	Genes_Fitness = []
	All_lists_genetic = []
	for i in range(4):
		Genes_Arrays.append(FirstGenerateABoard(BoardsSize))
		Genes_Fitness.append(fitness_function(Genes_Arrays[i]))
		
	i = 0;
	
	while i >= 0:
		All_lists_genetic.append(list(Genes_Arrays))
		print(i, ":", Genes_Arrays)
		for j in range(4):
			Genes_Fitness[j] = fitness_function(Genes_Arrays[j])
		Genes_Arrays, Genes_Fitness = chooseBest(Genes_Arrays, Genes_Fitness)
		
		for gen in Genes_Arrays:
			if (Valid(gen)):
				return True, gen, All_lists_genetic
		
		CG1, CG2 = crossOver(Genes_Arrays[0], Genes_Arrays[1])
		CG3, CG4 = crossOver(Genes_Arrays[1], Genes_Arrays[2])
		
		mCG1 = mutate(CG1)
		mCG2 = mutate(CG2)
		mCG3 = mutate(CG3)
		mCG4 = mutate(CG4)
		
		Genes_Arrays[0] = mCG1;
		Genes_Arrays[1] = mCG2;
		Genes_Arrays[2] = mCG3;
		Genes_Arrays[3] = mCG4;
		i = i + 1
	return None


def main():
	NSize = 7
	
	print("genetic_Algorithm")
	print(Genetic_Algorithm(NSize))


if __name__ == '__main__':
	main()
