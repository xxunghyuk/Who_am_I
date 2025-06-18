import Foundation

struct Candidate {
    var name = "Sung"
    var background = ["Music School", "DSP", "Machine Learning"]
    var traits = ["fast learner", "obsessed with debugging", "systems thinker"]
    var projects = ["CarRacing RL Agent", "TinyML DSP Classifier", "VR Concert Debugging"]

    func simulateGrowth(epoch: Int) -> String {
        for _ in 1...epoch {
            learn(from: .failure)
            update(weights: .curiosity, optimizer: .perseverance)
        }
        return "Ready for FEA Team deployment"
    }

    func apply(to company: String) -> String {
        if company == "Apple" {
            return "Design meets Engineering. This is my natural habitat."
        } else {
            return "Still learning, but my heart's at Apple."
        }
    }
}

enum InputChallenge {
    case failure
    case undefinedBug
    case tightDeadline
}

enum Weight: String {
    case curiosity, resilience, creativity
}

enum Optimizer {
    case perseverance, collaboration
}

// Simulation
let sung = Candidate()
print(sung.simulateGrowth(epoch: 2025))
print(sung.apply(to: "Apple"))