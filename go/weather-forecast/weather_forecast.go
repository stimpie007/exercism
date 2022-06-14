// Package weather forecasts the weather for given location.
package weather

// CurrentCondition is a string of the weather condition.
var CurrentCondition string

// CurrentLocation is a string of the city.
var CurrentLocation string

// Forecast states the condition for the given city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
