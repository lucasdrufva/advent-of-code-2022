//
//  main.swift
//  aoc-day1
//
//  Created by Lucas Drufva on 2022-12-06.
//

import Foundation


// File stored in documents folder
let file = "input1.txt"

var result = ""

//if you get access to the directory
if let dir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
 
    //prepare file url
    let fileURL = dir.appendingPathComponent(file)
 
    do {
        result = try String(contentsOf: fileURL, encoding: .utf8)
    }
    catch {/* handle if there are any errors */}
}

var calories:[Int] = []
let elfs = result.components(separatedBy: "\n\n")
for elf in elfs{
    calories.append(elf.components(separatedBy: "\n").map { Int($0)! }.reduce(0, +))
}

print("Part 1: \(calories.max()!)")

let sorted_cals = calories.sorted { $0 > $1 }

print("Part 2: \(sorted_cals[0...2].reduce(0, +))")

