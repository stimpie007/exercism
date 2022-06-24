package lasagna

import "strings"

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, prepTime int) int {
	if prepTime == 0 {
		return 2
	}
	return len(layers) * prepTime
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	layersString := strings.Join(layers, ",")
	noodles := strings.Count(layersString, "noodles")
	sauce := strings.Count(layersString, "sauce")
	return noodles * 50, float64(sauce) * 0.02
}

// TODO: define the 'AddSecretIngredient()' function

// TODO: define the 'ScaleRecipe()' function
