takze
helm install prefect prefect/prefect-orion --namespace=prefect -f .\prefect\values.yaml
funguje
Nefunguje to kdyz jsem zkousel lokalni,
pze se neprepisovaly values

Zaroven to vypada, ze kdyz
specifiku PW, tak se DB nevytvori s
tim PW. Jen se to nastavi na tom orion podu. Takze skopirovat PW z DB a pak to pujde