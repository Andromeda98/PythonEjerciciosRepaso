list1 = [3, 4, 57, 33, 4, 66, 3, 22]
list2 = [2, 5, 76, 34, 12, 4, 5, 7]

def son_iguales(arr1, arr2):
    # Primero verificar longitud
    if len(arr1) != len(arr2):
        return False
    
    # Luego verificar elemento por elemento
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    
    return True

if son_iguales(list1, list2):
    print("✅ Los arrays son exactamente iguales")
else:
    print("❌ Los arrays NO son iguales")