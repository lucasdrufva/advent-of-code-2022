data = File.read!("input1") |> String.trim()
elfs = String.split(data, "\n\n")

sum_calories = fn(part) ->
  String.split(part, "\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.sum()
end

# Part 1
part1 = Enum.map(elfs, sum_calories)
        |> Enum.max()

IO.puts("Part1:")
IO.puts(part1)

# Part 2
part2 = Enum.map(elfs, sum_calories)
        |> Enum.sort(:desc)
        |> Enum.take(3)
        |> Enum.sum()

IO.puts("Part2:")
IO.puts(part2)

