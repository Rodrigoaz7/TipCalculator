# ***** Aqui esta localizado a funcao de retorno
import numpy as np
import skfuzzy as fuzz

def fuzzifier(nota_qualidade, nota_servico):

	# Generate universe variables
	#   * Quality and service on subjective ranges [0, 10]
	#   * Tip has a range of [0, 25] in units of percentage points
	x_qual = np.arange(0, 11, 1)
	x_serv = np.arange(0, 11, 1)
	x_tip  = np.arange(0, 26, 1)

	# Generate fuzzy membership functions
	qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
	qual_md = fuzz.trimf(x_qual, [0, 5, 10])
	qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
	serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
	serv_md = fuzz.trimf(x_serv, [0, 5, 10])
	serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
	tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
	tip_md = fuzz.trimf(x_tip, [0, 13, 25])
	tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

	# We need the activation of our fuzzy membership functions at these values.
	# The exact values 6.5 and 9.8 do not exist on our universes...
	# This is what fuzz.interp_membership exists for!
	qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, nota_qualidade)
	qual_level_md = fuzz.interp_membership(x_qual, qual_md, nota_qualidade)
	qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, nota_qualidade)

	serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, nota_servico)
	serv_level_md = fuzz.interp_membership(x_serv, serv_md, nota_servico)
	serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, nota_servico)

	# Now we take our rules and apply them. Rule 1 concerns bad food OR service.
	# The OR operator means we take the maximum of these two.
	active_rule1 = np.fmax(qual_level_lo, serv_level_lo)

	# Now we apply this by clipping the top off the corresponding output
	# membership function with `np.fmin`
	tip_activation_lo = np.fmin(active_rule1, tip_lo)  # removed entirely to 0

	# For rule 2 we connect acceptable service to medium tipping
	tip_activation_md = np.fmin(serv_level_md, tip_md)

	# For rule 3 we connect high service OR high food with high tipping
	active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
	tip_activation_hi = np.fmin(active_rule3, tip_hi)
	tip0 = np.zeros_like(x_tip)

	# Aggregate all three output membership functions together
	aggregated = np.fmax(tip_activation_lo,
	                     np.fmax(tip_activation_md, tip_activation_hi))

	# Calculate defuzzified result
	# ----------THIS IS THE ANWSER------------------
	tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
	#------------------------------------------------

	return tip



