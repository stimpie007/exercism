package meteorology

import "fmt"

type TemperatureUnit int

const (
	Celsius    TemperatureUnit = 0
	Fahrenheit TemperatureUnit = 1
)

// Add a String method to the TemperatureUnit type
func (t *TemperatureUnit) String() string {
	switch *t {
	case Celsius:
		return "°C"
	case Fahrenheit:
		return "°F"
	default:
		return "Not an implemented unit"
	}
}

type Temperature struct {
	degree int
	unit   TemperatureUnit
}

// Add a String method to the Temperature type
func (t *Temperature) String() string {
	return fmt.Sprintf("%d %s", t.degree, t.unit.String())
}

type SpeedUnit int

const (
	KmPerHour    SpeedUnit = 0
	MilesPerHour SpeedUnit = 1
)

// Add a String method to SpeedUnit
func (s *SpeedUnit) String() string {
	switch *s {
	case KmPerHour:
		return "km/h"
	case MilesPerHour:
		return "mph"
	default:
		return "Not an implemented unit"
	}
}

type Speed struct {
	magnitude int
	unit      SpeedUnit
}

// Add a String method to Speed
func (s *Speed) String() string {
	return fmt.Sprintf("%d %s", s.magnitude, s.unit.String())
}

type MeteorologyData struct {
	location      string
	temperature   Temperature
	windDirection string
	windSpeed     Speed
	humidity      int
}

// Add a String method to MeteorologyData
func (m *MeteorologyData) String() string {
	return fmt.Sprintf(
		"%s: %d %s, Wind %s at %d %s, %d%% Humidity",
		m.location,
		m.temperature.degree,
		&m.temperature.unit,
		m.windDirection,
		m.windSpeed.magnitude,
		&m.windSpeed.unit,
		m.humidity)
}
