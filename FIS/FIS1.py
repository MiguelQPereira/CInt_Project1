import simpful as sf



FS1 = sf.FuzzySystem()

# Output network throughtput
S1_1 = sf.FuzzySet(points=[[0, 1.], [0.4, 0.2], [0.50, 0]], term="low_output")
S1_2 = sf.FuzzySet(points=[[0.3, 0], [0.45, 1.], [0.55, 1.], [0.7, 0]], term="medium_output")
S1_3 = sf.FuzzySet(points=[[0.5, 0], [0.6, 0.2], [1, 1.]], term="high_output")
FS1.add_linguistic_variable("NET_OUTPUT", sf.LinguisticVariable([S1_1, S1_2, S1_3]))

# Avalable output bandwidth
S2_1 = sf.FuzzySet(points=[[0, 1.], [0.4, 0.2], [0.50, 0]], term="low_band")
S2_2 = sf.FuzzySet(points=[[0.3, 0], [0.45, 1.], [0.55, 1.], [0.7, 0]], term="medium_band")
S2_3 = sf.FuzzySet(points=[[0.5, 0], [0.6, 0.2], [1, 1.]], term="high_band")
FS1.add_linguistic_variable("BANDWIDTH", sf.LinguisticVariable([S2_1, S2_2, S2_3]))

# Latency
S3_1 = sf.FuzzySet(points=[[0, 1.], [0.4, 0.2], [0.50, 0]], term="low_latency")
S3_2 = sf.FuzzySet(points=[[0.3, 0], [0.45, 1.], [0.55, 1.], [0.7, 0]], term="medium_latency")
S3_3 = sf.FuzzySet(points=[[0.5, 0], [0.6, 0.2], [1, 1.]], term="high_latency")
FS1.add_linguistic_variable("LATENCY", sf.LinguisticVariable([S3_1, S3_2, S3_3]))

# Output
FS1.set_output_function("LOWER_CLP", "max(-1, min(1, ((0.5 * LATENCY + 0.3 * NET_OUTPUT + 0.2 * BANDWIDTH) / 3)))")
FS1.set_output_function("MAINTAIN_CLP", "max(-1, min(1, ((0.5 * LATENCY + 0.3 * NET_OUTPUT + 0.2 * BANDWIDTH) / 3)))")
FS1.set_output_function("INCREASE_CLP", "max(-1, min(1, ((0.5 * LATENCY + 0.3 * NET_OUTPUT + 0.2 * BANDWIDTH) / 3)))")

# Rules:

RULE1 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS low_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE2 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS medium_latency) THEN (CLP IS INCREASE_CLP)"
RULE3 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE4 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE5 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE6 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE7 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE8 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE9 = "IF (NET_OUTPUT IS low_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"


RULE10 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE11 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE12 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE13 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE14 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE15 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE16 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE17 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE18 = "IF (NET_OUTPUT IS medium_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"


RULE19 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE20 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE21 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS low_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE22 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE23 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS medium_latency) THEN (CLP IS MAINTAIN_CLP)"
RULE24 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS medium_band) AND (LATENCY IS high_latency) THEN (CLP IS INCREASE_CLP)"

RULE25 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS low_latency) THEN (CLP IS LOWER_CLP)"
RULE26 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS medium_latency) THEN (CLP IS LOWER_CLP)"
RULE27 = "IF (NET_OUTPUT IS high_output) AND (BANDWIDTH IS high_band) AND (LATENCY IS high_latency) THEN (CLP IS MAINTAIN_CLP)"

FS1.add_rules([RULE1, RULE2, RULE3, RULE4, RULE5, RULE6, RULE7, RULE8, RULE9, RULE10, RULE11, RULE12, RULE13, RULE14, RULE15, RULE16, RULE17, RULE18, RULE19, RULE20, RULE21, RULE22, RULE23, RULE24, RULE25, RULE26, RULE27])



FS1.set_variable("NET_OUTPUT", .8)
FS1.set_variable("BANDWIDTH",.3)
FS1.set_variable("LATENCY", .4)
print(FS1.Sugeno_inference(['CLP']))