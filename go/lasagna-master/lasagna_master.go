package lasagna

import "strings"

func PreparationTime(layers []string, prepTime int) int {
	if prepTime == 0 {
		return 2
	}
	return len(layers) * prepTime
}

func Quantities(layers []string) (int, float64) {
	layersString := strings.Join(layers, ",")
	noodles := strings.Count(layersString, "noodles")
	sauce := strings.Count(layersString, "sauce")
	return noodles * 50, float64(sauce) * 0.2
}

func AddSecretIngredient(friendsList, myList []string) {
	myList = append(myList, friendsList...)
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, portion int) {
	for i := range quantities {
		quantities[i] *= (float64(portion) / 2)
	}
}
