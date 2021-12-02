(define (domain lisak)

  (:requirements :strips)

  (:predicates
    (square ?sqr)
    (coordinate ?x ?y)
    (empty ?x ?y)
    (at ?sqr ?x ?y)
  )

  (:action move_x
    :parameters (?sqr ?x ?y ?new_x)
    :precondition (and (square ?sqr) (coordinate ?x ?y) (at ?sqr ?x ?y) (coordinate ?new_x ?y) (empty ?new_x ?y))
    :effect (and 
        (at ?sqr ?new_x ?y) 
        (not (at ?sqr ?x ?y)) 
        (empty ?x ?y) 
        (not (empty ?new_x ?y))
    )
  )

  (:action move_y
    :parameters (?sqr ?x ?y ?new_y)
    :precondition (and (square ?sqr) (coordinate ?x ?y) (at ?sqr ?x ?y) (coordinate ?x ?new_y) (empty ?x ?new_y))
    :effect (and 
        (at ?sqr ?x ?new_y) 
        (not (at ?sqr ?x ?y)) 
        (empty ?x ?y) 
        (not (empty ?x ?new_y))
    )
  )

)
