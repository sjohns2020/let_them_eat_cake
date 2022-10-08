import pdb
from models.baker import Baker
from models.cake import Cake

import repositories.baker_repository as baker_repository
import repositories.cake_repository as cake_repository

cake_repository.delete_all()
baker_repository.delete_all()

baker_1 = Baker("Kyle Gorman", "You know what I mean", 3, 17000)
baker_repository.save(baker_1)

baker_2 = Baker("Danielle Tausney", "I love my job", 8, 24000)
baker_repository.save(baker_2)

baker_repository.select_all()

cake_1 = Cake("Victoria Sponge", 10, 2, 4, baker_1, "Birthday Cake", True, 4, 6)
cake_repository.save(cake_1)
cake_2 = Cake("Chocolate Egg Cake", 5, 2, 4, baker_2, "Easter Cake", False, 10, 13)
cake_repository.save(cake_2)




pdb.set_trace()