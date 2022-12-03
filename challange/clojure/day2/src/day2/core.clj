(ns day2.core
  (:gen-class))

(require '[clojure.string :as str])

(defn to_number_pair [x] (list (- (int (.charAt (first x) 0)) 65) (- (int (.charAt (first (rest x)) 0)) 88)))



(defn outcome [x y] (if (= x y) 3 (if (= (mod (+ x 1) 3) (mod (+ y 2) 3) ) 0 6))) 

(defn calc_score [x y] (+ y 1 (outcome x y) ) )

(defn calc_move [x y] (case y
                        0 (get [2 0 1] x)
                        1 x
                        2 (mod (+ x 1) 3)))

(defn part1 [pairs] (reduce +(map #(calc_score (first %) (first (rest %))) pairs )))

(defn part2 [pairs] (reduce +(map #(calc_score (first %) (calc_move (first %) (first (rest %)))) pairs )))


(defn -main
  [& args]
  (print "Part 1: ")
  (println (part1 (read_file)))
  (print "Part 2: ")
  (println (part2 (read_file))))
