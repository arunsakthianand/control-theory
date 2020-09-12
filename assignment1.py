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

print("For ratio of polynomials,");
print("\nThe numerator is "); 
printPoly( multiply( N0, ( multiply( N1, ( multiply( N2,N3 ) ) ) ) ) ); 
print("\nThe denominator is "); 
printPoly( multiply( D1, ( multiply( D2, ( multiply( D3, ( multiply( D4,D5 ) ) ) ) ) ) ) );  

