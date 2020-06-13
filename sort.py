
secuencia = [5,2,4,1]

def bubble_sort(array):

    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def merge_sort(array, low, high):
    if low < high:
        #divide and conquer
        length = len(array)
        mid = (low + high)/2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1,high)
        def merge(arr, l, m, h):
            #calcula la mitad del sub arreglo
            n1 = m-l+1
            n2 = h-m
            #crea sub arreglo 1
            for i in range(n1):
                new_arr1[i] = arr[l+1]
            #crea sub arreglo 2
            for j in range(n2):
                new_arr2[j] = arr[m+j+1
            for k in range(length):
                if 

            


    

def quick_sort(array):
    pass

def selector_ordenamiento(num):
    if num == 1:
        secuencia_ordenada = bubble_sort(secuencia)
        print(secuencia_ordenada)
        print('Metodo ordenado por Bubble Sort')
    elif num == 2:
        secuencia_ordenada = merge_sort(secuencia, low, high)
        print(secuencia_ordenada)
        print('Metodo ordenado por Merge Sort')
    else:
        secuencia_ordenada = quick_sort(secuencia)
        print(secuencia_ordenada)
        print('Metodo ordenado por Quick Sort')


def run():
    print('1. Bubble Sort \n2. Merge Sort \n3. Quick Sort')
    seleccion = int(input('Seleccione metodo ordenamiento: '))
    print(f'La secuencia original es {secuencia}')
    selector_ordenamiento(seleccion)
    


if __name__ == '__main__':
    run()