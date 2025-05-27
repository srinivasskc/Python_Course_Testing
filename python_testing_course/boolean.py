is_raining  = True
is_sunny = False
is_windy = True
is_snowing = False
is_cloudy = True

print(f'is_raining: {is_raining}')
print(f'is_sunny: {is_sunny}')
print(f'is_windy: {is_windy}')
print(f'is_snowing: {is_snowing}')
print(f'is_cloudy: {is_cloudy}')

# Boolean Operations

a = 5
b = 10
result = a > b
print(f'result of a > b: {result}')  # False

bad_Weathear = is_raining or is_snowing or is_windy  # T or F or T = True
print(f'Is the weather bad?:  {bad_Weathear}')  # True if any of the conditions are True

good_weather = is_sunny and not is_raining and not is_windy  # F and T and T = False
print(f'Is the weather good?: {good_weather}')  # True if it is sunny and not raining or windy