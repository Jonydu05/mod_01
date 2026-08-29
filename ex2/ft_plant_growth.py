class Plant:
	def __init__(self, name: str, height: float, days: int, growth_value: float):
		self.name = name
		self.height = height
		self.days = days
		self.growth_value = growth_value
	
	def show(self):
		print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

	def grow(self, days_passed: int):
		self.height += self.growth_value * days_passed

	def age(self, days_passed: int):
		self.grow(days_passed)
		self.days += days_passed


if __name__ == "__main__":
	rose = Plant("Rose", 25, 30, 0.8)
	print("=== Garden Plant Growth ===")
	rose.show()
	for i in range(1, 8):
		print(f"=== Day {i} ===")
		rose.age(1)
		rose.show()
	print(f"Growth this week: {(rose.growth_value * i):.1f}cm")
