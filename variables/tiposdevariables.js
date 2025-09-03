
//String 
var nombre = 'Gonzalo'

// Numeros
var edad = 200

// Boolean
var esLunes = true
var esMartes = false

/* console.log(nombre, edad, esLunes)
nombre = "Pedro"

console.log(nombre, edad, esLunes) */

// constantes
const clima = "Soleado"


// Arreglos Arrays
const miArray = ["perro", "gato", "conejo", 12, true]
const nums = [0, 4, 3, 0]
/* console.log(miArray)
console.log(miArray.length) */


var twoSum = function (nums, target) {
  var resultado  = []
  var resultadoSuma = 0
  if (nums.length > 2) { 
    for (let indice1 = 0; indice1 < nums.length; indice1++) {
      for (let indice2 = 0; indice2 < nums.length; indice2++) {
        console.log(nums[indice1] + nums[indice2])
        if (nums[indice1] + nums[indice2] == target && indice1 != indice2 && resultado.length <= 1) {
          resultado.push(indice1)
          resultado.push(indice2)
          break
        }
      }
    }
  } else if (nums.length == 2) {
    if (nums[0] + nums[1] == target) {
      resultado = [0, 1]
    }
  }

  return resultado
};

console.log(twoSum([0, 4, 3, 0], 0))
twoSum()

var gato = 'canela'
var edad = 5
var esmacho = false
if (gato == 'kitty') {
  console.log('hola soy kitty')
}
else {
console.log('no me llamo kitty')
}