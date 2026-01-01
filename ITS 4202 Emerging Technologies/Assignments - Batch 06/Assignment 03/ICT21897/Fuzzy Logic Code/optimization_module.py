"""
Part 6: Optimization Module
Genetic Algorithm and Particle Swarm Optimization for Fuzzy Parameter Tuning
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Callable
import copy

# ============================================================================
# Genetic Algorithm Optimization
# ============================================================================

class GeneticAlgorithmOptimizer:
    """Optimize fuzzy membership function parameters using GA"""
    
    def __init__(self, population_size=50, generations=100, mutation_rate=0.1, crossover_rate=0.8):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.best_fitness_history = []
        self.avg_fitness_history = []
        
    def initialize_population(self):
        """Initialize random population of membership function parameters"""
        # Each chromosome represents [temp_cold, temp_optimal, temp_warm, 
        #                             humid_low, humid_optimal, humid_high]
        population = []
        for _ in range(self.population_size):
            chromosome = [
                np.random.uniform(12, 20),   # temp_cold
                np.random.uniform(20, 28),   # temp_optimal
                np.random.uniform(26, 34),   # temp_warm
                np.random.uniform(40, 60),   # humid_low
                np.random.uniform(60, 80),   # humid_optimal
                np.random.uniform(75, 95),   # humid_high
            ]
            population.append(chromosome)
        return population
    
    def fitness_function(self, chromosome, test_data):
        """
        Evaluate fitness of a chromosome
        Lower error = higher fitness
        """
        total_error = 0
        
        for temp_actual, humid_actual, stage, temp_target, humid_target in test_data:
            # Simulate controller with these parameters
            temp_error = abs(temp_actual - temp_target)
            humid_error = abs(humid_actual - humid_target)
            
            # Weighted error based on membership function parameters
            temp_weight = self._calculate_membership(temp_actual, chromosome[0:3])
            humid_weight = self._calculate_membership(humid_actual, chromosome[3:6])
            
            weighted_error = (temp_error * temp_weight + humid_error * humid_weight) / 2
            total_error += weighted_error
        
        # Return inverse of error (higher fitness for lower error)
        return 1.0 / (1.0 + total_error)
    
    def _calculate_membership(self, value, params):
        """Calculate triangular membership degree"""
        low, optimal, high = params
        
        if value <= low:
            return 1.0
        elif value <= optimal:
            return (optimal - value) / (optimal - low)
        elif value <= high:
            return (high - value) / (high - optimal)
        else:
            return 0.0
    
    def selection(self, population, fitness_scores):
        """Tournament selection"""
        selected = []
        for _ in range(self.population_size):
            # Tournament of 3
            tournament = np.random.choice(len(population), 3, replace=False)
            tournament_fitness = [fitness_scores[i] for i in tournament]
            winner_idx = tournament[np.argmax(tournament_fitness)]
            selected.append(copy.deepcopy(population[winner_idx]))
        return selected
    
    def crossover(self, parent1, parent2):
        """Single-point crossover"""
        if np.random.random() < self.crossover_rate:
            point = np.random.randint(1, len(parent1))
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            return child1, child2
        return parent1, parent2
    
    def mutate(self, chromosome):
        """Random mutation"""
        mutated = chromosome.copy()
        for i in range(len(mutated)):
            if np.random.random() < self.mutation_rate:
                # Add random noise
                noise = np.random.uniform(-5, 5)
                mutated[i] = max(0, min(100, mutated[i] + noise))
        return mutated
    
    def optimize(self, test_data):
        """Run genetic algorithm optimization"""
        print("\n🧬 GENETIC ALGORITHM OPTIMIZATION")
        print("-" * 70)
        
        # Initialize
        population = self.initialize_population()
        best_chromosome = None
        best_fitness = 0
        
        for generation in range(self.generations):
            # Evaluate fitness
            fitness_scores = [self.fitness_function(chromo, test_data) for chromo in population]
            
            # Track best
            gen_best_fitness = max(fitness_scores)
            gen_avg_fitness = np.mean(fitness_scores)
            
            self.best_fitness_history.append(gen_best_fitness)
            self.avg_fitness_history.append(gen_avg_fitness)
            
            if gen_best_fitness > best_fitness:
                best_fitness = gen_best_fitness
                best_chromosome = population[fitness_scores.index(gen_best_fitness)]
            
            # Progress update
            if (generation + 1) % 20 == 0:
                print(f"   Generation {generation + 1}/{self.generations} - "
                      f"Best Fitness: {gen_best_fitness:.4f}, Avg: {gen_avg_fitness:.4f}")
            
            # Selection
            selected = self.selection(population, fitness_scores)
            
            # Crossover and Mutation
            next_population = []
            for i in range(0, len(selected), 2):
                if i + 1 < len(selected):
                    child1, child2 = self.crossover(selected[i], selected[i + 1])
                    next_population.append(self.mutate(child1))
                    next_population.append(self.mutate(child2))
                else:
                    next_population.append(self.mutate(selected[i]))
            
            population = next_population
        
        print(f"\n✅ Optimization Complete!")
        print(f"   Best Fitness Achieved: {best_fitness:.4f}")
        print(f"   Best Parameters: {best_chromosome}")
        
        return best_chromosome, best_fitness

# ============================================================================
# Particle Swarm Optimization
# ============================================================================

class ParticleSwarmOptimizer:
    """Optimize fuzzy membership function parameters using PSO"""
    
    def __init__(self, num_particles=30, max_iterations=100, w=0.7, c1=1.5, c2=1.5):
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.w = w  # Inertia weight
        self.c1 = c1  # Cognitive parameter
        self.c2 = c2  # Social parameter
        self.best_fitness_history = []
        self.avg_fitness_history = []
        
    def initialize_swarm(self):
        """Initialize particle positions and velocities"""
        particles = []
        velocities = []
        
        for _ in range(self.num_particles):
            position = [
                np.random.uniform(12, 20),   # temp_cold
                np.random.uniform(20, 28),   # temp_optimal
                np.random.uniform(26, 34),   # temp_warm
                np.random.uniform(40, 60),   # humid_low
                np.random.uniform(60, 80),   # humid_optimal
                np.random.uniform(75, 95),   # humid_high
            ]
            velocity = [np.random.uniform(-2, 2) for _ in range(6)]
            
            particles.append(position)
            velocities.append(velocity)
        
        return particles, velocities
    
    def fitness_function(self, position, test_data):
        """Evaluate fitness of particle position"""
        total_error = 0
        
        for temp_actual, humid_actual, stage, temp_target, humid_target in test_data:
            temp_error = abs(temp_actual - temp_target)
            humid_error = abs(humid_actual - humid_target)
            
            temp_weight = self._calculate_membership(temp_actual, position[0:3])
            humid_weight = self._calculate_membership(humid_actual, position[3:6])
            
            weighted_error = (temp_error * temp_weight + humid_error * humid_weight) / 2
            total_error += weighted_error
        
        return 1.0 / (1.0 + total_error)
    
    def _calculate_membership(self, value, params):
        """Calculate triangular membership degree"""
        low, optimal, high = params
        
        if value <= low:
            return 1.0
        elif value <= optimal:
            return (optimal - value) / (optimal - low)
        elif value <= high:
            return (high - value) / (high - optimal)
        else:
            return 0.0
    
    def optimize(self, test_data):
        """Run PSO optimization"""
        print("\n🌊 PARTICLE SWARM OPTIMIZATION")
        print("-" * 70)
        
        # Initialize
        particles, velocities = self.initialize_swarm()
        personal_best_positions = particles.copy()
        personal_best_fitness = [self.fitness_function(p, test_data) for p in particles]
        
        global_best_position = personal_best_positions[np.argmax(personal_best_fitness)]
        global_best_fitness = max(personal_best_fitness)
        
        for iteration in range(self.max_iterations):
            for i in range(self.num_particles):
                # Update velocity
                r1, r2 = np.random.random(), np.random.random()
                
                cognitive = [self.c1 * r1 * (personal_best_positions[i][j] - particles[i][j]) 
                           for j in range(6)]
                social = [self.c2 * r2 * (global_best_position[j] - particles[i][j]) 
                         for j in range(6)]
                
                velocities[i] = [self.w * velocities[i][j] + cognitive[j] + social[j] 
                                for j in range(6)]
                
                # Update position
                particles[i] = [particles[i][j] + velocities[i][j] for j in range(6)]
                
                # Boundary constraints
                particles[i] = [max(0, min(100, particles[i][j])) for j in range(6)]
                
                # Evaluate fitness
                fitness = self.fitness_function(particles[i], test_data)
                
                # Update personal best
                if fitness > personal_best_fitness[i]:
                    personal_best_fitness[i] = fitness
                    personal_best_positions[i] = particles[i].copy()
                
                # Update global best
                if fitness > global_best_fitness:
                    global_best_fitness = fitness
                    global_best_position = particles[i].copy()
            
            # Track progress
            avg_fitness = np.mean(personal_best_fitness)
            self.best_fitness_history.append(global_best_fitness)
            self.avg_fitness_history.append(avg_fitness)
            
            if (iteration + 1) % 20 == 0:
                print(f"   Iteration {iteration + 1}/{self.max_iterations} - "
                      f"Best Fitness: {global_best_fitness:.4f}, Avg: {avg_fitness:.4f}")
        
        print(f"\n✅ Optimization Complete!")
        print(f"   Best Fitness Achieved: {global_best_fitness:.4f}")
        print(f"   Best Parameters: {global_best_position}")
        
        return global_best_position, global_best_fitness

# ============================================================================
# Optimization Visualization
# ============================================================================

def plot_optimization_results(ga_optimizer, pso_optimizer):
    """Plot optimization convergence"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle('Optimization Convergence Comparison', fontsize=16, fontweight='bold')
    
    # Genetic Algorithm
    axes[0].plot(ga_optimizer.best_fitness_history, 'b-', linewidth=2, label='Best Fitness')
    axes[0].plot(ga_optimizer.avg_fitness_history, 'b--', linewidth=2, alpha=0.6, label='Avg Fitness')
    axes[0].set_title('Genetic Algorithm')
    axes[0].set_xlabel('Generation')
    axes[0].set_ylabel('Fitness')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # PSO
    axes[1].plot(pso_optimizer.best_fitness_history, 'r-', linewidth=2, label='Best Fitness')
    axes[1].plot(pso_optimizer.avg_fitness_history, 'r--', linewidth=2, alpha=0.6, label='Avg Fitness')
    axes[1].set_title('Particle Swarm Optimization')
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Fitness')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def compare_before_after_optimization(original_params, optimized_params):
    """Compare parameters before and after optimization"""
    param_names = ['Temp Cold', 'Temp Optimal', 'Temp Warm', 
                   'Humid Low', 'Humid Optimal', 'Humid High']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(param_names))
    width = 0.35
    
    ax.bar(x - width/2, original_params, width, label='Original', alpha=0.8)
    ax.bar(x + width/2, optimized_params, width, label='Optimized', alpha=0.8)
    
    ax.set_title('Membership Function Parameters: Before vs After Optimization', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Parameter')
    ax.set_ylabel('Value')
    ax.set_xticks(x)
    ax.set_xticklabels(param_names, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    return fig

# ============================================================================
# Main Optimization Execution
# ============================================================================

def run_optimization():
    """Run optimization and compare results"""
    print("\n" + "="*70)
    print("PART 6: OPTIMIZATION OF FUZZY MEMBERSHIP PARAMETERS")
    print("="*70 + "\n")
    
    # Generate test data for optimization
    print("📊 Generating test data for optimization...")
    np.random.seed(42)
    test_data = []
    
    for _ in range(50):
        temp_actual = np.random.uniform(15, 30)
        humid_actual = np.random.uniform(50, 85)
        stage = np.random.choice([0, 1, 2])
        temp_target = np.random.uniform(20, 25)
        humid_target = np.random.uniform(60, 75)
        test_data.append((temp_actual, humid_actual, stage, temp_target, humid_target))
    
    print(f"✅ Generated {len(test_data)} test cases\n")
    
    # Original parameters (baseline)
    original_params = [18, 24, 30, 55, 70, 85]
    
    print("📌 Original Parameters:")
    print(f"   {original_params}\n")
    
    # Run Genetic Algorithm
    ga_optimizer = GeneticAlgorithmOptimizer(population_size=50, generations=100)
    ga_best_params, ga_best_fitness = ga_optimizer.optimize(test_data)
    
    # Run PSO
    pso_optimizer = ParticleSwarmOptimizer(num_particles=30, max_iterations=100)
    pso_best_params, pso_best_fitness = pso_optimizer.optimize(test_data)
    
    # Compare results
    print("\n" + "="*70)
    print("OPTIMIZATION RESULTS COMPARISON")
    print("="*70)
    
    # Calculate original fitness for comparison
    original_fitness = ga_optimizer.fitness_function(original_params, test_data)
    
    print(f"\n📊 Fitness Scores:")
    print(f"   Original Parameters:  {original_fitness:.4f}")
    print(f"   GA Optimized:         {ga_best_fitness:.4f} "
          f"(+{((ga_best_fitness - original_fitness) / original_fitness * 100):.1f}%)")
    print(f"   PSO Optimized:        {pso_best_fitness:.4f} "
          f"(+{((pso_best_fitness - original_fitness) / original_fitness * 100):.1f}%)")
    
    # Determine best optimizer
    if ga_best_fitness > pso_best_fitness:
        print(f"\n✅ WINNER: Genetic Algorithm")
        print(f"   Improvement: {((ga_best_fitness - original_fitness) / original_fitness * 100):.1f}%")
        best_params = ga_best_params
    else:
        print(f"\n✅ WINNER: Particle Swarm Optimization")
        print(f"   Improvement: {((pso_best_fitness - original_fitness) / original_fitness * 100):.1f}%")
        best_params = pso_best_params
    
    print("\n📈 Best Optimized Parameters:")
    print(f"   {[f'{p:.2f}' for p in best_params]}")
    
    # Visualizations
    print("\n\n🎨 Generating Optimization Visualizations...")
    print("-" * 70)
    
    fig1 = plot_optimization_results(ga_optimizer, pso_optimizer)
    fig2 = compare_before_after_optimization(original_params, best_params)
    
    # Save results
    print("\n💾 Saving Optimization Results...")
    print("-" * 70)
    
    import os
    output_dir = os.getcwd()
    
    fig1.savefig(os.path.join(output_dir, 'optimization_convergence.png'), dpi=300, bbox_inches='tight')
    print(f"   ✅ Convergence plot saved to: {output_dir}/optimization_convergence.png")
    
    fig2.savefig(os.path.join(output_dir, 'parameter_comparison.png'), dpi=300, bbox_inches='tight')
    print(f"   ✅ Parameter comparison saved to: {output_dir}/parameter_comparison.png")
    
    # Save optimization data
    optimization_results = {
        'Method': ['Original', 'Genetic Algorithm', 'Particle Swarm'],
        'Fitness': [original_fitness, ga_best_fitness, pso_best_fitness],
        'Improvement (%)': [
            0,
            ((ga_best_fitness - original_fitness) / original_fitness * 100),
            ((pso_best_fitness - original_fitness) / original_fitness * 100)
        ]
    }
    
    import pandas as pd
    df = pd.DataFrame(optimization_results)
    df.to_csv(os.path.join(output_dir, 'optimization_results.csv'), index=False)
    print(f"   ✅ Optimization results saved to: {output_dir}/optimization_results.csv")
    
    plt.show()
    
    print("\n" + "="*70)
    print("✅ OPTIMIZATION COMPLETED SUCCESSFULLY!")
    print("="*70 + "\n")
    
    return best_params, ga_optimizer, pso_optimizer

if __name__ == "__main__":
    run_optimization()