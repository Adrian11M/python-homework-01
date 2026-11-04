total_seconds = int(input("Seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Seconds: {total_seconds}")
print(f"{hours} h {minutes} min {seconds} s")