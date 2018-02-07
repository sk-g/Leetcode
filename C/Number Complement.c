/* 
476 Number Complement
 
 
*/
int findComplement(int num) {
    if(num==1) return 0;
    if(num==0) return 1;
    else{
        int x = (log(num)/log(2));
        int y =pow(2,x+1)-1;
        //int t=y-1;
    return num^y;
        
    }
}