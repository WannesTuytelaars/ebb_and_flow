#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define NUTRIENTS 12
void *balance_nut(double* concentrations, double* required_concentrations, double* masses_add){//concentrations are always in mg/L and volumes in L
    double volume_now = *(concentrations+NUTRIENTS);
    double volume_end = *(required_concentrations+NUTRIENTS);
    double masses[NUTRIENTS];
    for(int i = 0; i<NUTRIENTS; i++){
        masses_add[i] = *(required_concentrations + i) * volume_end - *(concentrations + i) * volume_now;
    masses_add[NUTRIENTS] = volume_end - volume_now;
    }    
    return  0;
}
// source: https://stakahama.gitlab.io/sie-eng270/C_intro.html