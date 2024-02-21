def calculate_remaining_length(wall_length, brick_length, num_bricks):

    total_brick_length = brick_length * num_bricks 


    remaining_length = wall_length - total_brick_length

    return remaining_length


wall_length = float(input("Enter the length of the wall: "))
wall_width = float(input("Enter the width of the wall: "))
wall_height = float(input("Enter the height of the wall: "))


brick_length = float(input("Enter the length of the brick: "))
brick_width = float(input("Enter the width of the brick: "))
brick_height = float(input("Enter the height of the brick: "))


num_bricks = int(input("Enter the number of bricks to insert: "))

remaining_length = calculate_remaining_length(wall_length, brick_length, num_bricks)
print(f"The remaining length of the wall after inserting {num_bricks} bricks is {remaining_length}.")