#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <logfile> [keyword]\n";
        return 1;
    }

    const std::string filepath = argv[1];
    const std::string keyword = (argc >= 3) ? argv[2] : "";

    std::ifstream file(filepath);
    if (!file.is_open()) {
        std::cerr << "Error: could not open file -> " << filepath << '\n';
        return 1;
    }

    std::vector<std::string> matched_lines;
    std::string line;

    while (std::getline(file, line)) {
        if (keyword.empty() || line.find(keyword) != std::string::npos) {
            matched_lines.push_back(line);
        }
    }

    for (const auto& entry : matched_lines) {
        std::cout << entry << '\n';
    }

    std::cout << "\nMatched lines: " << matched_lines.size() << '\n';
    return 0;
}
