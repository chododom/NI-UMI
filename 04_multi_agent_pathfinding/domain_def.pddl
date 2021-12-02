(define (domain MAPF)

  (:requirements :strips)

  (:predicates
	(node ?n)
	(agent ?a)
	(at ?a ?n)
        (next ?n1 ?n2)
        (empty ?n)
  )

  (:action move
	:parameters(?a ?n1 ?n2)
	:precondition( and (node ?n1) (agent ?a) (at ?a ?n1) (next ?n1 ?n2) (next ?n2 ?n1) (empty ?n2) )
	:effect (and 
	   (at ?a ?n2)
	   (not (at ?a ?n1)) 
	   (not (empty ?n2)) 
	   (empty ?n1) )
  )

)
