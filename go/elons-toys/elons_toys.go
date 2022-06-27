package elon

import "fmt"

func (c *Car) Drive() {
	if c.battery > c.batteryDrain {
		c.battery -= c.batteryDrain
		c.distance += c.speed
	}
}

func (c *Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %d meters", c.distance)
}

func (c *Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %d%%", c.battery)
}

func (c *Car) CanFinish(trackDistance int) bool {
	// Calculate the battery way
	// distancePerKM := trackDistance / c.speed
	// maxBattery := distancePerKM * c.batteryDrain
	// if maxBattery >= c.battery {
	// 	return true
	// } else {
	// 	return false
	// }
	return trackDistance/c.speed*c.batteryDrain <= c.battery

	// Calculate the distance way
	// maxBattery := c.battery / c.batteryDrain
	// maxDistance := c.speed * maxBattery
	// if maxDistance >= trackDistance {
	// 	return true
	// } else {
	// 	return false
	// }
	// return (c.battery/c.batteryDrain)*c.speed >= trackDistance
}
