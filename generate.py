#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                    EVM Wallet Generator                       ║
║                     Created by Flexoryn                       ║
║                    Advanced Edition v2.0                      ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
from datetime import datetime
from eth_account import Account
from mnemonic import Mnemonic
from pathlib import Path
import argparse

Account.enable_unaudited_hdwallet_features()

class Colors:
    """ANSI Color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class WalletGenerator:
    """Advanced EVM Wallet Generator with multiple features"""
    
    def __init__(self, output_dir="wallets"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def print_banner(self):
        """Display application banner"""
        banner = f"""
{Colors.OKCYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              ███████╗██╗     ███████╗██╗  ██╗ ██████╗        ║
║              ██╔════╝██║     ██╔════╝╚██╗██╔╝██╔═══██╗       ║
║              █████╗  ██║     █████╗   ╚███╔╝ ██║   ██║       ║
║              ██╔══╝  ██║     ██╔══╝   ██╔██╗ ██║   ██║       ║
║              ██║     ███████╗███████╗██╔╝ ██╗╚██████╔╝       ║
║              ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ║
║                                                               ║
║              EVM Wallet Generator - Advanced Edition         ║
║                     Created by Flexoryn                       ║
║                         Version 2.0                           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(banner)
    
    def generate_wallet(self, strength=128):
        """
        Generate a single EVM wallet
        
        Args:
            strength: Mnemonic strength (128=12 words, 256=24 words)
        
        Returns:
            tuple: (mnemonic, private_key, address)
        """
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=strength)
        acct = Account.from_mnemonic(mnemonic)
        private_key = acct.key.hex()
        address = acct.address
        return mnemonic, private_key, address
    
    def save_to_files(self, wallets, format_type="txt"):
        """
        Save wallets to files in different formats
        
        Args:
            wallets: List of wallet tuples
            format_type: Output format (txt, json, csv)
        """
        base_name = f"wallet_{self.timestamp}"
        
        if format_type == "json":
            self._save_json(wallets, base_name)
        elif format_type == "csv":
            self._save_csv(wallets, base_name)
        else:
            self._save_txt(wallets, base_name)
    
    def _save_txt(self, wallets, base_name):
        """Save wallets in separate TXT files"""
        mnemonic_file = self.output_dir / f"{base_name}_mnemonic.txt"
        privkey_file = self.output_dir / f"{base_name}_privatekeys.txt"
        address_file = self.output_dir / f"{base_name}_addresses.txt"
        
        with open(mnemonic_file, "w") as f_mnemonic, \
             open(privkey_file, "w") as f_privkey, \
             open(address_file, "w") as f_address:
            
            for mnemonic, privkey, address in wallets:
                f_mnemonic.write(f"{mnemonic}\n")
                f_privkey.write(f"{privkey}\n")
                f_address.write(f"{address}\n")
        
        print(f"\n{Colors.OKGREEN}✅ Files saved:{Colors.ENDC}")
        print(f"   📄 {mnemonic_file}")
        print(f"   📄 {privkey_file}")
        print(f"   📄 {address_file}")
    
    def _save_json(self, wallets, base_name):
        """Save wallets in JSON format"""
        json_file = self.output_dir / f"{base_name}.json"
        
        wallet_data = []
        for idx, (mnemonic, privkey, address) in enumerate(wallets, 1):
            wallet_data.append({
                "wallet_number": idx,
                "mnemonic": mnemonic,
                "private_key": privkey,
                "address": address,
                "created_at": datetime.now().isoformat()
            })
        
        with open(json_file, "w") as f:
            json.dump(wallet_data, f, indent=2)
        
        print(f"\n{Colors.OKGREEN}✅ JSON file saved:{Colors.ENDC}")
        print(f"   📄 {json_file}")
    
    def _save_csv(self, wallets, base_name):
        """Save wallets in CSV format"""
        csv_file = self.output_dir / f"{base_name}.csv"
        
        with open(csv_file, "w") as f:
            f.write("Wallet_Number,Mnemonic,Private_Key,Address\n")
            for idx, (mnemonic, privkey, address) in enumerate(wallets, 1):
                f.write(f"{idx},\"{mnemonic}\",{privkey},{address}\n")
        
        print(f"\n{Colors.OKGREEN}✅ CSV file saved:{Colors.ENDC}")
        print(f"   📄 {csv_file}")
    
    def display_wallet(self, idx, mnemonic, privkey, address):
        """Display wallet information in formatted style"""
        print(f"{Colors.OKCYAN}{'='*70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.OKGREEN}🔐 Wallet #{idx} | Flexoryn Generator{Colors.ENDC}")
        print(f"{Colors.OKCYAN}{'-'*70}{Colors.ENDC}")
        print(f"{Colors.WARNING}🧠 Mnemonic    :{Colors.ENDC} {mnemonic}")
        print(f"{Colors.OKBLUE}🔑 Private Key :{Colors.ENDC} {privkey}")
        print(f"{Colors.HEADER}🏦 Address     :{Colors.ENDC} {address}")
        print(f"{Colors.OKCYAN}{'='*70}{Colors.ENDC}\n")
    
    def batch_generate(self, count, strength=128, format_type="txt", show_output=True):
        """
        Generate multiple wallets in batch
        
        Args:
            count: Number of wallets to generate
            strength: Mnemonic strength (128 or 256)
            format_type: Output format (txt, json, csv)
            show_output: Display wallets in console
        """
        print(f"\n{Colors.BOLD}⚙️  Generating {count} EVM wallets...{Colors.ENDC}\n")
        
        wallets = []
        start_time = time.time()
        
        for i in range(1, count + 1):
            mnemonic, privkey, address = self.generate_wallet(strength)
            wallets.append((mnemonic, privkey, address))
            
            if show_output:
                self.display_wallet(i, mnemonic, privkey, address)
            else:
                # Progress indicator for large batches
                if i % 10 == 0 or i == count:
                    progress = (i / count) * 100
                    print(f"\r{Colors.OKGREEN}Progress: {i}/{count} ({progress:.1f}%){Colors.ENDC}", end='')
        
        if not show_output:
            print()  # New line after progress
        
        elapsed_time = time.time() - start_time
        
        # Save to files
        self.save_to_files(wallets, format_type)
        
        # Summary
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✅ Generation Complete!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}📊 Summary:{Colors.ENDC}")
        print(f"   • Total wallets: {count}")
        print(f"   • Mnemonic strength: {strength} bits ({12 if strength==128 else 24} words)")
        print(f"   • Time elapsed: {elapsed_time:.2f} seconds")
        print(f"   • Average: {elapsed_time/count:.3f} seconds per wallet")
        print(f"   • Output directory: {self.output_dir.absolute()}\n")

def main():
    """Main execution function"""
    generator = WalletGenerator()
    generator.print_banner()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Advanced EVM Wallet Generator by Flexoryn")
    parser.add_argument("-n", "--number", type=int, help="Number of wallets to generate")
    parser.add_argument("-s", "--strength", type=int, choices=[128, 256], default=128, 
                       help="Mnemonic strength: 128 (12 words) or 256 (24 words)")
    parser.add_argument("-f", "--format", choices=["txt", "json", "csv"], default="txt",
                       help="Output format")
    parser.add_argument("-q", "--quiet", action="store_true", 
                       help="Quiet mode (don't display wallets in console)")
    parser.add_argument("-o", "--output", default="wallets",
                       help="Output directory")
    
    args = parser.parse_args()
    
    # Interactive mode if no arguments provided
    if args.number is None:
        try:
            print(f"{Colors.BOLD}📥 Configuration:{Colors.ENDC}\n")
            
            jumlah = int(input(f"{Colors.OKBLUE}Enter number of wallets to generate: {Colors.ENDC}"))
            
            if jumlah <= 0:
                print(f"{Colors.FAIL}❌ Number must be greater than 0{Colors.ENDC}")
                return
            
            print(f"\n{Colors.OKBLUE}Select mnemonic strength:{Colors.ENDC}")
            print("  1. 128 bits (12 words) - Standard")
            print("  2. 256 bits (24 words) - Extra secure")
            strength_choice = input(f"{Colors.OKBLUE}Your choice [1/2, default=1]: {Colors.ENDC}").strip()
            strength = 256 if strength_choice == "2" else 128
            
            print(f"\n{Colors.OKBLUE}Select output format:{Colors.ENDC}")
            print("  1. TXT (Separate files)")
            print("  2. JSON (Single file)")
            print("  3. CSV (Single file)")
            format_choice = input(f"{Colors.OKBLUE}Your choice [1/2/3, default=1]: {Colors.ENDC}").strip()
            format_map = {"2": "json", "3": "csv"}
            format_type = format_map.get(format_choice, "txt")
            
            show_output = True
            if jumlah > 10:
                show = input(f"\n{Colors.WARNING}Display all wallets in console? [y/N]: {Colors.ENDC}").strip().lower()
                show_output = show == "y"
            
        except ValueError:
            print(f"{Colors.FAIL}❌ Invalid input. Please enter a valid number.{Colors.ENDC}")
            return
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}⚠️  Operation cancelled by user.{Colors.ENDC}")
            return
    else:
        jumlah = args.number
        strength = args.strength
        format_type = args.format
        show_output = not args.quiet
        
        if args.output != "wallets":
            generator.output_dir = Path(args.output)
            generator.output_dir.mkdir(exist_ok=True)
    
    # Generate wallets
    try:
        generator.batch_generate(jumlah, strength, format_type, show_output)
        print(f"{Colors.OKGREEN}{Colors.BOLD}🎉 All done! Stay safe and HODL! 🚀{Colors.ENDC}\n")
    except Exception as e:
        print(f"{Colors.FAIL}❌ Error occurred: {str(e)}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
