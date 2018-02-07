/* 69 Sqrt(x)
implement sqrt(int x)
Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Logic: deal with end case first. And then use Newton method
	to find integer square root. which is a solution of x^2-n=0
	giving Xk+1=0.5*(Xk+n/Xk) which converges to square root as k tends
	to inf.

*/
int mySqrt(int x) {
    if(x==0) return 0;
    else if(x<0) return NULL;
    else{
        long r = x;
    while (r*r > x)
        r = (r + x/r) / 2;
    return r;
        
    }
}