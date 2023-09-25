#!/bin/bash

# Solicita el primer número
echo "Introduce el primer número:"
read numero

# Verifica si el número es par o impar
if ((numero % 2 == 0))
then
  echo "El número $numero es par."
else
  echo "El número $numero es impar."
fi