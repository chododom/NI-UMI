(define (problem MAPF_instance)
    
    (:domain MAPF)

    (:objects
        pink light_blue green red yellow blue
        n1 n2 n3 n4 n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18
    )

    (:init
	(agent pink) (agent light_blue) (agent green) (agent red) (agent yellow) (agent blue)

	(node n1) (node n8) (node n7)
	(node n2)	    (node n6)
	(node n3) (node n4) (node n5)
			    (node n9) (node n10)
				      (node n11) (node n18) (node n17)
				      (node n12)	    (node n16)
				      (node n13) (node n14) (node n15)
        (next n1 n2) (next n2 n1)
	(next n2 n3) (next n3 n2)
	(next n3 n4) (next n4 n3)
	(next n4 n5) (next n5 n4)
	(next n5 n6) (next n6 n5)
	(next n6 n7) (next n7 n6)
	(next n7 n8) (next n8 n7)
	(next n1 n8) (next n8 n1)
	(next n5 n9) (next n9 n5)
	(next n9 n10) (next n10 n9)
	(next n10 n11) (next n11 n10)
	(next n11 n12) (next n12 n11)
	(next n12 n13) (next n13 n12)
	(next n13 n14) (next n14 n13)
	(next n14 n15) (next n15 n14)
	(next n15 n16) (next n16 n15)
	(next n16 n17) (next n17 n16)
	(next n17 n18) (next n18 n17)
	(next n18 n11) (next n11 n18)
        
        (at pink n1)
        (at light_blue n2)
        (at green n8)
        (at red n14)
        (at yellow n15)
        (at blue n16)

        (empty n3)
        (empty n4)
        (empty n5)
        (empty n6)
        (empty n7)
        (empty n9)
        (empty n10)
        (empty n11)
        (empty n12)
        (empty n13)
        (empty n18)
        (empty n17)
    )

    (:goal
        (and (at pink n15) (at green n11) (at light_blue n10) (at blue n9) (at red n5) (at yellow n1) )
    )
)
