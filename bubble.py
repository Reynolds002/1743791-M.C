def bubble(R):
	for u in range(1,len(R)-1):
		for v in range (0,len(R)-u):
			if (R[v+1]<R[v]):
				repuesto=R[v]
				R[v]=R[v+1]
				R[v+1]=repuesto			