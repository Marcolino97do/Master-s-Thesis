#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(void)
{
    int runs;
    long long int tim;
    int i,people,initmoney,a,b,exchange=1,seed;
    /*OPENING FILES*/
    FILE *param;
    FILE *results;
    param=fopen("param.txt","r");
    results=fopen("results.txt","r");
    if (param==NULL)
    {
        perror("Errore in apertura del file");
        exit(1);
    }
    if (results==NULL)
    {
        perror("Errore in apertura del file");
        exit(1);
    }
    fscanf(param,"%lli %d %d %d",&tim,&people,&initmoney,&runs);
    printf("parameters: %lli %d %d ",tim,people,initmoney);



    /* CREATING VECTORS*/
    int accounts[people];
    long long int t;
    for(i=0;i<people;i++)
    {
    fscanf(results,"%d\n",accounts[i]);
    }

    fclose(param);
    fclose(results);
    results=fopen("results.txt","w");

    /*EVOLUTION*/
    srand(time(NULL));
    seed=rand();
    for (t=0;t<tim/runs;t++)
    {
        a=(int)(((double)rand()/RAND_MAX)*people);
        b=(int)(((double)rand()/RAND_MAX)*people);
        /*b=(rand()+t%people)%people;*/

        if(accounts[a]>=exchange)
        {
            accounts[a]-=exchange;
            accounts[b]+=exchange;
        }
    }

    for(i=0;i<people;i++)
    {
    fprintf(results,"%d\n",accounts[i]);
    }

    fclose(param);
    fclose(results);
    return 0;
}