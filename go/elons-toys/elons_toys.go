package elon

// TODO: define the 'Drive()' method
func (c *Car) Drive() {
	c.battery -= c.batteryDrain
	c.distance += c.speed
}

// TODO: define the 'DisplayDistance() string' method

// TODO: define the 'DisplayBattery() string' method

// TODO: define the 'CanFinish(trackDistance int) bool' method
