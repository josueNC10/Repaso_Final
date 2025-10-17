import csv
import pandas as pd
def menu():
    while True:
        try:
            ventas = []
            print('\nMenú de opciones:')
            print('1. Registrar venta')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opción (1-4): '))
            
            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                guardar_ventas(ventas)   
            elif opcion == 3:
                consultar_ventas()
            elif opcion == 4:
                print('Saliendo del programa. ¡Hasta luego!')
                break
            else:
                print('Opción no válida. Por favor, seleccione una opción del 1 al 4.')

        except ValueError:
            print('Error: Entrada no válida. Por favor, ingrese un número del 1 al 4.')
            

def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (YYYY-MM-DD): ')
            cliente = input('Ingrese el nombre del cliente: ')
            
            if precio < 0 or cantidad < 0:
                print('El producto y la cantidad deben ser numeros positivos')
                continue
            
            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            
            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
               break

        except ValueError:
            print('Entrada no válida. Por favor, intente de nuevo.')
            continue

def guardar_ventas(ventas:list):
    try:
        if not ventas:
            print('No hay ventas para guardar.')
            return
        else:
            with open('ventas.csv', mode='w', newline='') as archivo:
                guardado = csv.DictWriter(archivo,fieldnames=['producto', 'cantidad', 'precio', 'fecha', 'cliente'])
                guardado.writeheader()
                guardado.writerows(ventas)
            print('Ventas guardadas exitosamente en ventas.csv')
    except Exception as e:
        print(f'\nError al guardar las ventas: {e}')

def consultar_ventas():
    try:
        df = pd.read_csv('ventas.csv')
        if df.empty:
            print('No hay ventas registradas.')
        else:
         print('\nVentas registradas:')
         df['subtotal'] = df['cantidad'] * df['precio']
         total = df['subtotal'].sum()
         print(f'Total de ventas: {total:.2f}')
         
         # Analisis de tendencias
         producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
         print(f'Producto más vendido: {producto_mas_vendido}')
         
         tendencia_clientes = df['cliente'].value_counts().idxmax()
         print(f'Cliente con más compras: {tendencia_clientes}')
    except FileNotFoundError:
        print('El archivo ventas.csv no existe. No hay ventas registradas.')
    except Exception as e:
        print(f'\nError al consultar las ventas: {e}')

#programa principal para gestionar ventas
if __name__ == "__main__": #verifica si el script se esta ejecutando directamente
    print('Bienvenido al sistema de gestion de ventas')
menu()    