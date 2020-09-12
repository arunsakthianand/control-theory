def multiply(A, B): 
	m = len(A); 
	n = len(B); 
	prod = [0] * (m + n - 1); 

	for i in range(m): 
		for j in range(n): 
			prod[i + j] += A[i] * B[j]; 
	return prod; 

def printPoly(poly): 
	n = len(poly);
	for i in range(n): 
		print(poly[i], end = ""); 
		if (i != 0): 
			print("s^", i, end = ""); 
		if (i != n - 1): 
			print(" + ", end = ""); 

N0 = [5];
N1 = [15,1];
N2 = [26,1];
N3 = [72,1];

D1 = [0,1];
D2 = [55,1];
D3 = [30,5,1];
D4 = [56,1];
D5 = [52,27,1];

print("For ratio of factors,");
print("\nThe numerator is "); 
print("(", end = '');
printPoly(N0);
print(")(", end = '');
printPoly(N1);
print(")(", end = '');
printPoly(N2);
print(")(", end = '');
printPoly(N3);
print(")", end = '');
print("\nThe denominator is "); 
print("(", end = '');
printPoly(D1);
print(")(", end = '');
printPoly(D2);
print(")(", end = '');
printPoly(D3);
print(")(", end = '');
printPoly(D4);
print(")(", end = '');
printPoly(D5);
print(")", end = '');
