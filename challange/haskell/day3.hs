import System.IO 
import Data.Char
import Data.List

calculate_priority :: Char -> Int
calculate_priority c
              | isUpper c = ((ord c) - (ord 'A') + 27)
              | otherwise = ((ord c) - (ord 'a') + 1)

sum_prioritys :: [Char] -> Int
sum_prioritys s = foldr (+) 0 (map calculate_priority s)

find_duplicates :: [Char] -> [Char]
find_duplicates s = nub $ left `intersect` right
            where middle = (length s) `div` 2
                  (left, right) = splitAt middle s

part1 :: [Char] -> Int
part1 input = foldr (+) 0 (map sum_prioritys duplicates)
      where duplicates = map find_duplicates (lines input)

part2 :: [[Char]] -> Int
part2 [] = 0
part2 (x:y:z:xs) = (calculate_priority (head (x `intersect` y `intersect` z))) + (part2 xs)


main = do
  inputs <- readFile "input3.txt"
  print (part1 inputs)
  print (part2 (lines inputs))

