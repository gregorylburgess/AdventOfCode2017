import math, sys

def av(x):
	# Special case for perfect odd square.
	det = math.sqrt(x)
	if  det % 2 == 1:
		return det - 1
	# Compute which layer we're in
	layer = math.floor( (det + 1) / 2.0 )
	# Compute the side length of our layer (square).
	side_len = 2 * layer + 1
	# Compute our index within our layer.
	previous_square = math.pow( 2 * (layer - 1) + 1, 2 )
	relative_pos = (x - previous_square) % (side_len - 1)
	# Compute the lateral distance to the center of our side.
	lateral_offset = abs( relative_pos - layer)
	# return lateral offset plus the ring layer (vertical offset).
	return lateral_offset + layer
	
if __name__ == "__main__":
	print av(float(sys.argv[1]))
