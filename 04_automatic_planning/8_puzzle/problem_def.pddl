(define (problem lisak_instance) 

    (:domain lisak)
    (:objects
	sqr1 sqr2 sqr3 sqr4 sqr5 sqr6 sqr7 sqr8
        x0 x1 x2
        y0 y1 y2
    )

    (:init
        (square sqr1) (square sqr2) (square sqr3) (square sqr4) (square sqr5) (square sqr6) (square sqr7) (square sqr8)
        (coordinate x0 y0) (coordinate x0 y1) (coordinate x0 y2)
        (coordinate x1 y0) (coordinate x1 y1) (coordinate x1 y2)
        (coordinate x2 y0) (coordinate x2 y1) (coordinate x2 y2)
        (empty x1 y1) 
	(at sqr1 x2 y2) 
	(at sqr2 x0 y1)
        (at sqr3 x2 y1) 
	(at sqr4 x0 y2) 	
	(at sqr5 x1 y0)
        (at sqr6 x1 y2) 
	(at sqr7 x0 y0) 
	(at sqr8 x2 y0)
    )

    (:goal (and 
		(at sqr1 x0 y0) 
		(at sqr2 x0 y1)
        	(at sqr3 x0 y2) 
		(at sqr4 x1 y0) 	
		(at sqr5 x1 y1)
        	(at sqr6 x1 y2) 
		(at sqr7 x2 y0) 
		(at sqr8 x2 y1)
		(empty x2 y2)
        )
    )

)
