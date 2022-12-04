(ns day1.core
  (:gen-class))

(require '[clojure.string :as str])

(defn read_file [] (slurp "input1.txt"))

(defn sum_elves [data]
  (map #(reduce + (map (fn [x] (Integer/parseInt x)) (str/split % #"\n"))) (str/split data #"\n\n")))

(defn part1 [elfs] (apply max elfs))

(defn part2 [elfs]
  (let [sorted (reverse (sort elfs))] (+ (first sorted) (first (rest sorted)) (first (rest (rest sorted))))))

(defn -main
  [& args]
  (let [elfs (sum_elves (read_file))]
    (print "Part1: ")
    (println (part1 elfs))
    (print "Part2: ")
    (println (part2 elfs))))
