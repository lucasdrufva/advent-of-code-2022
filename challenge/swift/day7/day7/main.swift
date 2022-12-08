//
//  main.swift
//  day7
//
//  Created by Lucas Drufva on 2022-12-07.
//

import Foundation

extension Array {

  var tail: Array {
    return Array(self.dropFirst())
  }

}

// File stored in documents folder
let file = "input7.txt"

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

enum NodeError: Error {
    case fileNotFound
}

class Node {
    let name:String;
    
    init(name: String) {
        self.name = name
    }
    
    func get_content_by_path(path:[String]) throws -> Node {
        if path[0] == self.name && path.count == 1{
            return self;
        }
        else {
            throw NodeError.fileNotFound;
        }
    }
    
    func traverse(condition: (Int) -> Bool, list: inout [Int]) -> Int {
        return 0;
    }
    
}

class File: Node {
    let size:Int;
    
    init(name: String, size: Int) {
        self.size = size;
        super.init(name: name);
    }
    
    override func traverse(condition: (Int) -> Bool, list: inout [Int]) -> Int {
        return size;
    }
}

class Directory: Node {
    var content = Dictionary<String, Node>();
    
    func add_content(_ item:Node){
        content[item.name] = item;
    }
    
    func add_content_by_path(path:[String], item:Node) throws{
        guard path[0] == self.name else {
            throw NodeError.fileNotFound;
        }
        
        if path.count == 1{
            content[item.name] = item;
            return;
        }
        
        if let val = content[path[1]] {
            if val is Directory{
                try (val as! Directory).add_content_by_path(path: path.tail, item:item);
                return;
            }
            else {
                throw NodeError.fileNotFound;
            }
        }

        throw NodeError.fileNotFound;
        
    }
    
    override func get_content_by_path(path:[String]) throws -> Node {
        guard path[0] == self.name else {
            throw NodeError.fileNotFound;
        }
                
        if let node = content[path[1]] {
            return try node.get_content_by_path(path: path.tail);
        }
        
        throw NodeError.fileNotFound;
        
    }
    
    override func traverse(condition: (Int) -> Bool, list: inout [Int]) -> Int {
        var size = 0;
        
        for (_, node) in content{
            size += node.traverse(condition: condition, list: &list);
        }
        
        if condition(size){
            list.append(size);
        }
        
        return size;
    }
    
}

var currentPath:[String] = [];
var tree = Directory(name: "/");

let lines = result.components(separatedBy: "\n");
for line in lines{
    let cdRegex = /\$ cd (.+)/
    if let res = line.firstMatch(of: cdRegex){
        if res.1 == ".."{
            _ = currentPath.popLast();
        }
        else{
            currentPath.append(String(res.1));
        }
    }
    
    let dirRegex = /dir (.+)/
    if let res = line.firstMatch(of: dirRegex){
        try tree.add_content_by_path(path: currentPath, item: Directory(name: String(res.1)));
    }
    
    let fileRegex = /(\d+) (.+)/
    if let res = line.firstMatch(of: fileRegex){
        try tree.add_content_by_path(path: currentPath, item: File(name: String(res.2), size: Int(res.1)!));
    }
}

var smallFolders:[Int] = [];
var total = tree.traverse(condition: { $0 <= 100000  }, list: &smallFolders);

print("Part 1: \(smallFolders.reduce(0, +))");

var bigFolders:[Int] = [];
let space_to_free = 30000000-(70000000-total);
_ = tree.traverse(condition: { $0 >= space_to_free}, list: &bigFolders);
bigFolders.sort();

print("Part 2: \(bigFolders[0])");
