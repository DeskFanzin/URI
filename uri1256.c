#include <stdio.h>
#include <stdlib.h>

typedef struct __list{
	struct lista *proxlista;
	int data;
} Lista;

typedef struct __ultimal{
	Lista *primeiro;
	Lista *ultimo;
} UltimaLista;

void Dispers(UltimaLista *oi, int y, int x){
	int calculo = y % x;
	Lista *opa = NULL;
	opa = (Lista *) malloc(sizeof(Lista));
	if (oi[calculo].primeiro)
	  oi[calculo].ultimo->proxlista = opa;
	else
		oi[calculo].primeiro = opa;
	oi[calculo].ultimo = opa;
	opa->data = y;
  opa->proxlista = NULL;
}

int main (){
    Lista *j;
    int n,x, y, i, k, l;
    scanf("%d", &n);
    for (k=0;k<n;k++){
      scanf("%d%d",&x,&y);
      UltimaLista resp[x];
      for (i=0;i<x;++i)
        resp[i].primeiro = NULL, resp[i].ultimo = NULL;
      for (i=0;i<y;++i){
        scanf("%d", &l);
        Dispers(resp, l, x);
      }
      for (i=0; i<x;++i){	
        printf("%d -> ", i);
        for (j = resp[i].primeiro; j; j = j->proxlista)
          printf("%d -> ", j->data);
        printf("\\\n");
      }
      if (k+1<n)
        printf("\n");
    }
    free(j);
    return 0;
}
